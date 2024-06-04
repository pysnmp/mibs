#
# PySNMP MIB module IANA-PWE3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iana/IANA-PWE3-MIB
# Produced by pysmi-1.1.12 at Tue Jun  4 14:07:31 2024
# On host fv-az693-600 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, mib_2, NotificationType, TimeTicks, ModuleIdentity, iso, Counter64, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, MibIdentifier, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "mib-2", "NotificationType", "TimeTicks", "ModuleIdentity", "iso", "Counter64", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "MibIdentifier", "Integer32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaPwe3MIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 174))
ianaPwe3MIB.setRevisions(('2009-06-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ianaPwe3MIB.setRevisionsDescriptions(('Original version, published as part of RFC 5601.',))
if mibBuilder.loadTexts: ianaPwe3MIB.setLastUpdated('200906110000Z')
if mibBuilder.loadTexts: ianaPwe3MIB.setOrganization('IANA')
if mibBuilder.loadTexts: ianaPwe3MIB.setContactInfo('Internet Assigned Numbers Authority\n         Internet Corporation for Assigned Names and Numbers\n         4676 Admiralty Way, Suite 330\n         Marina del Rey, CA 90292-6601\n\n         Phone: +1 310 823 9358\n         EMail: iana@iana.org')
if mibBuilder.loadTexts: ianaPwe3MIB.setDescription("This MIB module defines the IANAPwTypeTC and\n        IANAPwPsnTypeTC textual conventions for use in PWE3\n        MIB modules.\n\n        Any additions or changes to the contents of this MIB\n        module require either publication of an RFC, Designated\n        Expert Review as defined in RFC 5226, Guidelines for\n        Writing an IANA Considerations Section in RFCs, and should\n        be based on the procedures defined in [RFC4446].  The\n        Designated Expert will be selected by the IESG Area\n        Director(s) of the internet Area.\n\n        Copyright (c) 2009 IETF Trust and the persons identified as\n        authors of the code.  All rights reserved.\n\n        Redistribution and use in source and binary forms, with or\n        without modification, are permitted provided that the\n\n        following conditions are met:\n\n        - Redistributions of source code must retain the above\n          copyright notice, this list of conditions and the\n          following disclaimer.\n\n        - Redistributions in binary form must reproduce the above\n          copyright notice, this list of conditions and the\n          following disclaimer in the documentation and/or other\n          materials provided with the distribution.\n\n        - Neither the name of Internet Society, IETF or IETF Trust,\n          nor the names of specific contributors, may be used to\n          endorse or promote products derived from this software\n          without specific prior written permission.\n\n        THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND\n        CONTRIBUTORS 'AS IS' AND ANY EXPRESS OR IMPLIED WARRANTIES,\n        INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF\n        MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE\n        DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR\n        CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,\n        INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES\n        (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE\n        GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR\n        BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF\n        LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT\n        (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT\n        OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE\n        POSSIBILITY OF SUCH DAMAGE. ")
class IANAPwTypeTC(TextualConvention, Integer32):
    description = 'Indicates the PW type (i.e., the carried service). '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 32767))
    namedValues = NamedValues(("other", 0), ("frameRelayDlciMartiniMode", 1), ("atmAal5SduVcc", 2), ("atmTransparent", 3), ("ethernetTagged", 4), ("ethernet", 5), ("hdlc", 6), ("ppp", 7), ("cem", 8), ("atmCellNto1Vcc", 9), ("atmCellNto1Vpc", 10), ("ipLayer2Transport", 11), ("atmCell1to1Vcc", 12), ("atmCell1to1Vpc", 13), ("atmAal5PduVcc", 14), ("frameRelayPortMode", 15), ("cep", 16), ("e1Satop", 17), ("t1Satop", 18), ("e3Satop", 19), ("t3Satop", 20), ("basicCesPsn", 21), ("basicTdmIp", 22), ("tdmCasCesPsn", 23), ("tdmCasTdmIp", 24), ("frDlci", 25), ("wildcard", 32767))

class IANAPwPsnTypeTC(TextualConvention, Integer32):
    description = 'Identifies the PSN type that the PW will use over the\n       network.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("mpls", 1), ("l2tp", 2), ("udpOverIp", 3), ("mplsOverIp", 4), ("mplsOverGre", 5), ("other", 6))

class IANAPwCapabilities(TextualConvention, Bits):
    description = 'This TC describes a collection of capabilities related to\n       a specific PW.\n       Values may be added in the future based on new capabilities\n       introduced in IETF documents.\n      '
    status = 'current'
    namedValues = NamedValues(("pwStatusIndication", 0), ("pwVCCV", 1))

mibBuilder.exportSymbols("IANA-PWE3-MIB", IANAPwPsnTypeTC=IANAPwPsnTypeTC, IANAPwTypeTC=IANAPwTypeTC, ianaPwe3MIB=ianaPwe3MIB, PYSNMP_MODULE_ID=ianaPwe3MIB, IANAPwCapabilities=IANAPwCapabilities)
