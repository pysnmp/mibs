#
# PySNMP MIB module MCAFEE-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mcafee/MCAFEE-SMI
# Produced by pysmi-1.1.12 at Fri Nov 22 15:13:26 2024
# On host fv-az692-788 platform Linux version 6.5.0-1025-azure by user runner
# Using Python version 3.10.15 (main, Sep  9 2024, 03:02:45) [GCC 11.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Integer32, Counter32, IpAddress, NotificationType, MibIdentifier, TimeTicks, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, ObjectIdentity, iso, Counter64, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Integer32", "Counter32", "IpAddress", "NotificationType", "MibIdentifier", "TimeTicks", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "ObjectIdentity", "iso", "Counter64", "Gauge32", "Bits")
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
mibBuilder.exportSymbols("MCAFEE-SMI", mcafeeGATEWAY=mcafeeGATEWAY, PYSNMP_MODULE_ID=mcafee, mcafee=mcafee)
