#
# PySNMP MIB module CORERO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/corero/CORERO-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 05:18:49 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ObjectIdentity, Counter32, TimeTicks, Unsigned32, iso, Integer32, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, ModuleIdentity, enterprises, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "Counter32", "TimeTicks", "Unsigned32", "iso", "Integer32", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "ModuleIdentity", "enterprises", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
corero = ModuleIdentity((1, 3, 6, 1, 4, 1, 41036))
corero.setRevisions(('2017-06-16 00:00', '2014-04-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: corero.setRevisionsDescriptions(('Updated contact info.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: corero.setLastUpdated('201706160000Z')
if mibBuilder.loadTexts: corero.setOrganization('Corero Network Security')
if mibBuilder.loadTexts: corero.setContactInfo('        Corero Support\n             E-mail: support.portal@corero.com')
if mibBuilder.loadTexts: corero.setDescription('Corero Management Server MIB.')
coreroRegistrations = ObjectIdentity((1, 3, 6, 1, 4, 1, 41036, 1))
if mibBuilder.loadTexts: coreroRegistrations.setStatus('current')
if mibBuilder.loadTexts: coreroRegistrations.setDescription('This module defines the enterprises OID for Corero Network Security.')
coreroProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 41036, 2))
if mibBuilder.loadTexts: coreroProducts.setStatus('current')
if mibBuilder.loadTexts: coreroProducts.setDescription('A registration point under which all Corero AGENT-CAPABILIITES\n         definitions (and therefore values of sysObjectId) are defined.')
mibBuilder.exportSymbols("CORERO-MIB", PYSNMP_MODULE_ID=corero, corero=corero, coreroProducts=coreroProducts, coreroRegistrations=coreroRegistrations)
