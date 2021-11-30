#
# PySNMP MIB module PT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/protelevision/PT-MIB
# Produced by pysmi-1.1.3 at Tue Nov 30 13:45:56 2021
# On host fv-az77-605 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibIdentifier, Integer32, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Counter64, ObjectIdentity, TimeTicks, Gauge32, IpAddress, NotificationType, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibIdentifier", "Integer32", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Counter64", "ObjectIdentity", "TimeTicks", "Gauge32", "IpAddress", "NotificationType", "iso", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pt = ModuleIdentity((1, 3, 6, 1, 4, 1, 18086))
pt.setRevisions(('2014-08-08 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pt.setRevisionsDescriptions(('PTT General Device MIB File',))
if mibBuilder.loadTexts: pt.setLastUpdated('201408081200Z')
if mibBuilder.loadTexts: pt.setOrganization('Protelevision Technologies, Denmark')
if mibBuilder.loadTexts: pt.setContactInfo('Contact:\n\n                Web: http://www.protelevision.com\n\n                Address: Valhoejs Alle 176, DK-2610 Roedovre, Denmark\n                Telephone: +45 44700000\n                Fax:       +45 44700001')
if mibBuilder.loadTexts: pt.setDescription('This is the root MIB module for PT with OID of\n                {iso org dod internet private enterprises 18086}.\n\n                Copyright (c) 2004 Protelevision Technologies A/S. All rights reserved.\n                Reproduction of this document is authorized on the condition\n                that the foregoing copyright notice is included.\n\n                IANA allocated this enterprise OID (object identifier) for the\n                exclusive use of Protelevision Technologies A/S (PT). \n                Other than internet network equipment\n                distributed or licensed by PT, no other party has any right\n                what-so-ever to distribute or license internet network equipment\n                which responds to the PT enterprise OID or its subsidiary\n                branches. PT reserves the right to criminally prosecute and/or\n                to seek civil damages from anyone fraudently using the PT\n                enterprise OID to the full extent of the law.')
mibBuilder.exportSymbols("PT-MIB", PYSNMP_MODULE_ID=pt, pt=pt)
