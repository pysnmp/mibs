#
# PySNMP MIB module MCAFEE-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mcafee/MCAFEE-SMI
# Produced by pysmi-1.1.8 at Fri Sep  8 07:43:31 2023
# On host fv-az268-298 platform Linux version 5.15.0-1041-azure by user runner
# Using Python version 3.10.13 (main, Aug 28 2023, 08:28:42) [GCC 11.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, iso, Counter64, Gauge32, ObjectIdentity, Counter32, Unsigned32, MibIdentifier, Integer32, enterprises, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Counter64", "Gauge32", "ObjectIdentity", "Counter32", "Unsigned32", "MibIdentifier", "Integer32", "enterprises", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mcafee = ModuleIdentity((1, 3, 6, 1, 4, 1, 1230))
mcafee.setRevisions(('2006-09-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mcafee.setRevisionsDescriptions(('Initial Definition',))
if mibBuilder.loadTexts: mcafee.setLastUpdated('200607110000Z')
if mibBuilder.loadTexts: mcafee.setOrganization('McAfee, Inc.')
if mibBuilder.loadTexts: mcafee.setContactInfo('McAfee Customer Service Department\n\n                         Postal: 5000 Headquarters Drive\n                         Plano, TX  75024\n                         USA\n\n                         Tel: +1 800 338 8754\n\n                         E-mail: support@mcafee.com')
if mibBuilder.loadTexts: mcafee.setDescription(' The Structure of Management Information for the\n\t\t  McAfee enterprise.')
mcafeeGATEWAY = ObjectIdentity((1, 3, 6, 1, 4, 1, 1230, 2))
if mibBuilder.loadTexts: mcafeeGATEWAY.setStatus('current')
if mibBuilder.loadTexts: mcafeeGATEWAY.setDescription('McAfee Gateway Products')
mibBuilder.exportSymbols("MCAFEE-SMI", mcafee=mcafee, PYSNMP_MODULE_ID=mcafee, mcafeeGATEWAY=mcafeeGATEWAY)
