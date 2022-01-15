#
# PySNMP MIB module SNMP-USM-AES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/SNMP-USM-AES-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 04:23:20 2022
# On host fv-az39-968 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
snmpPrivProtocols, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "snmpPrivProtocols")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, snmpModules, Counter64, Gauge32, ModuleIdentity, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, MibIdentifier, TimeTicks, Bits, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "snmpModules", "Counter64", "Gauge32", "ModuleIdentity", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "MibIdentifier", "TimeTicks", "Bits", "NotificationType", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snmpUsmAesMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 20))
snmpUsmAesMIB.setRevisions(('2004-06-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: snmpUsmAesMIB.setRevisionsDescriptions(('Initial version, published as RFC3826',))
if mibBuilder.loadTexts: snmpUsmAesMIB.setLastUpdated('200406140000Z')
if mibBuilder.loadTexts: snmpUsmAesMIB.setOrganization('IETF')
if mibBuilder.loadTexts: snmpUsmAesMIB.setContactInfo('Uri Blumenthal\n                  Lucent Technologies / Bell Labs\n                  67 Whippany Rd.\n                  14D-318\n                  Whippany, NJ  07981, USA\n                  973-386-2163\n                  uri@bell-labs.com\n\n                  Fabio Maino\n                  Andiamo Systems, Inc.\n                  375 East Tasman Drive\n                  San Jose, CA  95134, USA\n                  408-853-7530\n                  fmaino@andiamo.com\n\n                  Keith McCloghrie\n                  Cisco Systems, Inc.\n                  170 West Tasman Drive\n                  San Jose, CA  95134-1706, USA\n\n                  408-526-5260\n                  kzm@cisco.com')
if mibBuilder.loadTexts: snmpUsmAesMIB.setDescription("Definitions of Object Identities needed for\n                  the use of AES by SNMP's User-based Security\n                  Model.\n\n                  Copyright (C) The Internet Society (2004).\n\n            This version of this MIB module is part of RFC 3826;\n            see the RFC itself for full legal notices.\n            Supplementary information may be available on\n            http://www.ietf.org/copyrights/ianamib.html.")
usmAesCfb128Protocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 2, 4))
if mibBuilder.loadTexts: usmAesCfb128Protocol.setStatus('current')
if mibBuilder.loadTexts: usmAesCfb128Protocol.setDescription('The CFB128-AES-128 Privacy Protocol.')
if mibBuilder.loadTexts: usmAesCfb128Protocol.setReference('- Specification for the ADVANCED ENCRYPTION\n                    STANDARD. Federal Information Processing\n                    Standard (FIPS) Publication 197.\n                    (November 2001).\n\n                  - Dworkin, M., NIST Recommendation for Block\n                    Cipher Modes of Operation, Methods and\n                    Techniques. NIST Special Publication 800-38A\n                    (December 2001).\n                 ')
mibBuilder.exportSymbols("SNMP-USM-AES-MIB", PYSNMP_MODULE_ID=snmpUsmAesMIB, usmAesCfb128Protocol=usmAesCfb128Protocol, snmpUsmAesMIB=snmpUsmAesMIB)
