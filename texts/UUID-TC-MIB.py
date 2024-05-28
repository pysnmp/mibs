#
# PySNMP MIB module UUID-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/UUID-TC-MIB
# Produced by pysmi-1.1.12 at Tue May 28 12:12:46 2024
# On host fv-az1490-484 platform Linux version 6.5.0-1021-azure by user runner
# Using Python version 3.10.14 (main, May  8 2024, 15:05:35) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Integer32, mib_2, Bits, Counter32, NotificationType, Gauge32, ObjectIdentity, Counter64, Unsigned32, iso, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "mib-2", "Bits", "Counter32", "NotificationType", "Gauge32", "ObjectIdentity", "Counter64", "Unsigned32", "iso", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
uuidTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 217))
uuidTCMIB.setRevisions(('2013-04-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: uuidTCMIB.setRevisionsDescriptions(('Initial version of this MIB as published in\n                     RFC 6933.',))
if mibBuilder.loadTexts: uuidTCMIB.setLastUpdated('201304050000Z')
if mibBuilder.loadTexts: uuidTCMIB.setOrganization('IETF Energy Management Working Group')
if mibBuilder.loadTexts: uuidTCMIB.setContactInfo('WG Email: eman@ietf.org\n                     Mailing list subscription info:\n                     http://www.ietf.org/mailman/listinfo/eman\n\n                     Dan Romascanu\n                     Avaya\n                     Park Atidim, Bldg. #3\n                     Tel Aviv, 61581\n                     Israel\n                     Phone: +972-3-6458414\n                     Email: dromasca@avaya.com\n\n                     Juergen Quittek\n                     NEC Europe Ltd.\n                     Network Research Division\n                     Kurfuersten-Anlage 36\n                     Heidelberg  69115\n                     Germany\n                     Phone: +49 6221 4342-115\n                     Email: quittek@neclab.eu\n\n                     Mouli Chandramouli\n                     Cisco Systems, Inc.\n                     Sarjapur Outer Ring Road\n                     Bangalore 560103\n                     India\n                     Phone: +91 80 4429 2409\n                     Email: moulchan@cisco.com')
if mibBuilder.loadTexts: uuidTCMIB.setDescription("This MIB module defines TEXTUAL-CONVENTIONs\n                   representing Universally Unique IDentifiers\n                   (UUIDs).\n\n                   Copyright (c) 2013 IETF Trust and the persons\n                   identified as authors of the code.  All rights\n                   reserved.\n\n                   Redistribution and use in source and binary forms,\n                   with or without modification, is permitted\n                   pursuant to, and subject to the license terms\n                   contained in, the Simplified BSD License set forth\n                   in Section 4.c of the IETF Trust's Legal\n                   Provisions Relating to IETF Documents\n                   (http://trustee.ietf.org/license-info).")
class UUID(TextualConvention, OctetString):
    description = 'Universally Unique Identifier information.  The syntax must\n          conform to RFC 4122, Section 4.1.'
    status = 'current'
    displayHint = '4x-2x-2x-1x1x-6x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class UUIDorZero(TextualConvention, OctetString):
    description = 'Universally Unique Identifier information.  The syntax must\n          conform to RFC 4122, Section 4.1.\n\n          The semantics of the value zero-length OCTET STRING are\n          object-specific and must therefore be defined as part of\n          the description of any object that uses this syntax.'
    status = 'current'
    displayHint = '4x-2x-2x-1x1x-6x'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(16, 16), )
mibBuilder.exportSymbols("UUID-TC-MIB", uuidTCMIB=uuidTCMIB, UUID=UUID, UUIDorZero=UUIDorZero, PYSNMP_MODULE_ID=uuidTCMIB)
