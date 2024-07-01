#
# PySNMP MIB module CORERO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/corero/CORERO-MIB
# Produced by pysmi-1.1.12 at Mon Jul  1 10:52:21 2024
# On host fv-az665-510 platform Linux version 6.5.0-1022-azure by user runner
# Using Python version 3.10.14 (main, Jun 20 2024, 15:20:03) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Integer32, ModuleIdentity, NotificationType, iso, ObjectIdentity, Counter32, MibIdentifier, Bits, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Integer32", "ModuleIdentity", "NotificationType", "iso", "ObjectIdentity", "Counter32", "MibIdentifier", "Bits", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CORERO-MIB", coreroRegistrations=coreroRegistrations, corero=corero, coreroProducts=coreroProducts, PYSNMP_MODULE_ID=corero)
